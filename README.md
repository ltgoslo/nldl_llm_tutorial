# NLDL 2025 Winter School: tutorial on Large Language Models Under the Hood

## Contents

1. [Introduction on training deep neural networks](https://github.com/ltgoslo/nldl_llm_tutorial/blobP/main/slides/nldl_01_dnn.pdf)
2. Pre-training of Language Models; Masked and Generative Language Models
3. Hands-on: Generating and evaluating summaries with LLMs.

## Instructions
- Connect to your virtual machine, using the SSH key and ip address from the slides (`ssh -i naic_key naic-user@ip`)
- Start Jupyter Lab: `jupyter lab --no-browser --ip=0.0.0.0 --port=8888`
- In its output, find the URL with the security token (something like `http://127.0.0.1:8888/lab?token=XXXXX`)
- Copy-paste the full URL to your web browser address bar and replace `127.0.0.1` with the real ip of your virtual machine (see above)
- Now you have a fully functional Jupyter Lab in your browser which uses the resources of the virtual machine.
- The tutorial notebooks can be found at `/home/naic-user/shared/repo/nldl_llm_tutorial/code/`
- You can also use Python directly on the VM via SSH, without Jupyter, if you want.
