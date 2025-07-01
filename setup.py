# Importing Libraries
from setuptools import find_packages, setup
#from typing import List


# Decription of the local package 
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

# Define metadata variables
__version__ = '0.0.1'
src_name = 'recommendation-system'
author_name = 'Satkar'
author_user_name = 'Zenith40'
src_repo = 'recommendationSystem'      # name of folder inside  the src
author_email = 'zenith04u@gmail.com'

# Function to read requirements.txt file
'''HYPEN_E_DOT = '-e.'
def get_requirements(file_path:str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
'''


# Package Information
setup(
    name = src_repo,
    version = __version__,
    author = author_name,
    author_email = 'zenith04u@gmail.com',
    description = 'Recommendation system + RAG Chatbot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = f"https://github.com/{author_user_name}/{src_name}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{author_user_name}/{src_name}/issues"
    },
    package_dir={'':'src'},
    packages = find_packages(where='src'),
    #install_requires = get_requirements('requirements.txt')
)