import yaml



def read():
    with open("config.yml",'r', encoding='utf-8') as file:
        res = yaml.load(file.read(), Loader=yaml.FullLoader)
        print(res)

read()
