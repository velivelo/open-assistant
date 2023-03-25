from setuptools import setup


setup(
    name= "open_assistant",
    version= "1.0.0",
    description= "Assistant using Large Language Models",
    author= "Clément Mébarki",
    author_email= "m_clement@live.fr",
    packages= ["open_assistant", "open_assistant.models"],
    package_data= { "open_assistant": ["system.txt"] },
)