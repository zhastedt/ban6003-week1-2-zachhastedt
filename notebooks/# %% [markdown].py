# %% [markdown]
# # Week 1: Codespaces Readiness Check
# **BAN 6003 Data Management and Analytics Integration**
# 
# Welcome to the first course notebook. This notebook is intentionally short. Its purpose is to confirm that your GitHub Codespaces environment can run Python and import Pandas.
# 
# By the end of this notebook, you should be able to:
# - Open a notebook in GitHub Codespaces.
# - Run a code cell.
# - Confirm that Python and Pandas are working.
# - Add a short self-introduction.
# - Save, commit, and push your work to GitHub.
# 

# %% [markdown]
# ## How to Run a Cell
# Click inside the code cell below and press **Shift + Enter**, or simply click play button on top right corner. If you get a prompt window asking which enviroment to run, choose `Python Environments` then `base`.
#  
# 
# If you see a greeting message and a Pandas version number, your environment is working.
# 

# %%
print("✅ Hello BAN 6003! Your Codespaces environment is working.")

import pandas as pd
print(f"Pandas version: {pd.__version__}")


# %% [markdown]
# ## About You
# Edit this markdown cell and replace the prompts below with your own information.
# 
# - **Name:** [Zach Hastedt]
# - **Course section:** [BAN-6003-002, BAN-6003-ON1]
# - **Prior experience:** [The experience I have prior to this course include data analysis through excel. I am comfortable filtering and sorting important data, but aside from that I am no where near a pro at Excel or any other system.]
# - **One thing I hope to learn in this course:** [How to code properly.]
# 

# %% [markdown]
# ## A Tiny Python Test
# The cell below creates a variable and prints it. You do not need to understand every detail yet. For now, focus on running the cell and reading the output.
# 

# %%
course = "BAN 6003"
message = "I am ready to start working with data."

print(course)
print(message)


# %% [markdown]
# ## Save, Commit, and Push
# After you have run the cells and completed the **About You** section, save this notebook.
# 
# Then open the Terminal and run:
# 
# ```bash
# git add .
# git commit -m "Completed Week 1 setup"
# git push
# ```
# 
# You may commit and push more than once. Each push updates your assignment repository.
# 

# %% [markdown]
# ## Week 1 Completion Checklist
# Before you finish, make sure:
# 
# - [yes] I opened this notebook in GitHub Codespaces.
# - [yes] I selected the correct kernel if prompted.
# - [yes] I ran the Python/Pandas test cell successfully.
# - [yes] I completed the **About You** section.
# - [yes] I saved the notebook.
# - [yes] I committed and pushed my work to GitHub.
# - [yes] I stopped or deleted my Codespace after pushing my work.
# 


