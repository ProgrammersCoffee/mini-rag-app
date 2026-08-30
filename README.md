# mini-rag

this is a minimal implementation of the RAG model for question answering  

# 01,02,03  

# to make anew environment using conda

conda create -n mini-rag-app

# to activate conda environment

cond activate mini-rag-app

# WSL => windows sub system of linux => run sub system of linux on windows

# make that inside the terminal of windows subsystem of linux in the vcode  

 wget <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>

# to make miniconda executable make that prompt

chmod+x Miniconda3-latest-Linux-x86_64.sh

# to install this file

./Miniconda3-latest-Linux-x86_64.sh

# to install conda environment  

 conda create -n mini-rag-app python=3.8

# to activate conda environment

cond activate mini-rag-app

# Make conda to turn automically even open the wsl

conda init bash  
source ~/.bashrc   # After that



# to install conda environment  

 conda create -n mini-rag-app python=3.8  

# to activate miniconda

 conda activate /home/mohamed/miniconda3 

# 004

# after all the changes

 make in source control; -> init project directory
# installation after make creation of conda env ,activation 
## install required packages 
$ pip install -r requirements.txt 
### set up the environment variables 
 cp .env.example .env 
set your environment variables in the `.env` file. like `OPENAI_API_KEY` value. 

# run the fast api server 
# to make any change done in real-time >>- --reload   
uvicorn main:app --reload --host 0.0.0.0 --port 5000
