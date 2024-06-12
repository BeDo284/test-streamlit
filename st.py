import pandas
import streamlit as st
from datetime import *
import pandas as pd


class Item:
    def __init__(self, code: str, name: str, description: str, item_type: str, price: str, stock: str, minimum: str,
                 maximum=None):
        self.code = code
        self.name = name
        self.description = description
        self.item_type = item_type
        self.price = float(price)
        self.stock = int(stock)
        self.minimum = int(minimum)
        self.maximum = int(minimum) if maximum is None else maximum

    def value(self):
        return self.price * self.stock

    def shortage(self):
        return 0 if self.stock >= self.minimum else self.stock - self.minimum

    def order(self):
        return 0 if self.stock >= self.minimum else self.maximum - self.stock

    def adjust_stock(self, amount):
        if amount > 0:
            if amount > self.stock:
                raise ValueError(f"Not enough stock to transfer. Available stock: {self.stock}")
            self.stock -= amount
        else:
            self.stock += abs(amount)

    def toDict(self):
        return {
            'code': self.code,
            'name': self.name,
            'description': self.description,
            'item_type': self.item_type,
            'price': self.price,
            'stock': self.stock,
            'minimum': self.minimum,
            'maximum': self.maximum
        }


class Project:
    def __init__(self, name: str, description: str, items=None, readme=str):
        self.name = name
        self.description = description
        self.items = {} if items is None else items
        self.readme = readme
        self.creation_date = datetime.today()

    def addItem(self, item: Item, amount: int):
        if item.code not in self.items:
            self.items[item.code] = (item, 0)
        item.adjust_stock(amount)
        current_item, current_amount = self.items[item.code]
        self.items[item.code] = (current_item, current_amount + amount)

    def removeItem(self, item_code, amount: int):
        if item_code not in self.items:
            raise ValueError(f"Item '{item_code}' not found in project.")
        current_item, current_amount = self.items[item_code]
        if amount > current_amount:
            raise ValueError(f"Not enough stock to transfer back. Available in project: {current_amount}")
        current_item.adjust_stock(-amount)
        self.items[item_code] = (current_item, current_amount - amount)
        if self.items[item_code][1] == 0:
            del self.items[item_code]

    def worth(self):
        return sum(item.price * item.stock for item in self.items.values())


item_list = []
project_list = []
item1 = Item(code="001", name="Widget", description="A useful widget", item_type="Tool",
             price="19.99", stock="100", minimum="10", maximum="200")

project1 = Project(name="Project Alpha", description="A project for developing Alpha widgets",
                   readme="This project focuses on developing and improving widgets.")

print(f"Before adding item to project: {item1}")
project1.addItem(item1, 50)
print(f"After adding item to project: {item1}")
print(f"Project details: {project1}")
item2 = Item(code="002", name="Gadget", description="A fancy gadget", item_type="Accessory",
             price="29.99", stock="200", minimum="5", maximum="150")

item_list.append(item1)
item_list.append(item2)
project_list.append(project1)

project1.addItem(item2, 75)

print(f"After adding another item to project: {item2}")
print(f"Project details: {project1}")

print(f"Before removing item from project: {item1}")
project1.removeItem("001", 30)
print(f"After removing item from project: {item1}")
print(f"Project details: {project1}")

# ----------------------------------------------------------------------------------

# Initialize a session state for storing items
if 'items' not in st.session_state:
    st.session_state.items = []

st.title('Inventory management')
data = []
for item in item_list:
    data.append({"name": item.name, "code": item.code, "stock": item.stock})

df = pd.DataFrame(data)

st.write("### Items DataFrame")
st.dataframe(df)


#---------------------------