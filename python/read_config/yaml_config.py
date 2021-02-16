import yaml

with open(r'./configs/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    quantity = config["quantity"]
    items = config["items"]
    region = config["region"]

    output = f"Lets get {quantity} {items[0]} setup in {region}!!"

    print(f"\n{output}\n")