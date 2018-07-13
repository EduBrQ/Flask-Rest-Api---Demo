from setuptools import setup, find_packages

setup(
    name='rest_api_analytics',
    version='1.0.0',
    description='Microserviço para predição de dados da saúde, baseado na estrutura Flask-RESTPlus',
    url='https://github.com/EduBQr/ALPHA', 
    #'ANALYTIC LEARNING PROJECT FOR HEALTH ASSISTENCE'
    author='Eduardo Borba',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rest restful api flask swagger machine learning data science',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)
