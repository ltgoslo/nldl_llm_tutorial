import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from time import time
from tqdm import tqdm
import os

start = time()

tokenizer = AutoTokenizer.from_pretrained(sys.argv[1], clean_up_tokenization_spaces=False)
model = AutoModelForCausalLM.from_pretrained(sys.argv[1], torch_dtype=torch.bfloat16).eval()

end = time()

print(f"Loading the model took {int(end - start)} seconds")

questions = ["Hva er navnet på flyplassen i Moss?", "Hvor lenge har Rygge vært stengt?", "Hvem er talsperson for RSL?", "Hva svarer Espen Ettre på spørsmålet om han fortsatt er optimistisk?"]
responses = []

start = time()

for question in tqdm(questions):
    messages = [
        {"role": "user", "content": question}
    ]
    gen_input = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

    output = model.generate(
        gen_input,
        max_new_tokens=12,
        top_k=64,  # top-k sampling
        top_p=0.9,  # nucleus sampling
        temperature=0.3,  # a low temperature to make the outputs less chaotic
        repetition_penalty=1.0,  # turn the repetition penalty off, having it on can lead to very bad outputs
        do_sample=True,  # randomly sample the outputs
        use_cache=True,  # speed-up generation,
        pad_token_id=tokenizer.eos_token_id
    )
    decoded_output = tokenizer.decode(output[0, gen_input.size(1):], skip_special_tokens=True).strip()
    responses.append(decoded_output)

end = time()
for q, r in zip(questions, responses):
    print(q)
    print(r)
    print("====================")
print(f"Generating responses took {int(end - start)} seconds")

