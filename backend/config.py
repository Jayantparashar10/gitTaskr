import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///project_management.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    AZURE_DEVOPS_PAT = os.getenv('AZURE_DEVOPS_PAT', 'your_azure_devops_pat')
    AZURE_DEVOPS_ORG = os.getenv('AZURE_DEVOPS_ORG', 'your_azure_devops_org')
