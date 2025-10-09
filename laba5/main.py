# main.py
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from faker import Faker
import pyjokes
from bs4 import BeautifulSoup
from colorama import Fore, Style
from tqdm import tqdm
import time

try:
    response = requests.get("https://api.github.com")
    print("1. requests:", response.status_code, "✅")
except Exception as e:
    print("Помилка в requests:", e)
try:
    data = pd.DataFrame({
        "name": ["Artem", "Maks", "Olena"],
        "age": [20, 22, 19]
    })
    print("\n2. pandas:\n", data)
except Exception as e:
    print("Помилка в pandas:", e)
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("\n3. numpy сума:", np.sum(arr))
except Exception as e:
    print("Помилка в numpy:", e)
try:
    plt.plot([1, 2, 3], [2, 4, 6])
    plt.title("Простий графік")
    plt.savefig("plot.png")
    plt.close()
    print("\n4. matplotlib: збережено 'plot.png'")
except Exception as e:
    print("Помилка в matplotlib:", e)
try:
    fake = Faker()
    print("\n5. faker ім’я:", fake.name())
except Exception as e:
    print("Помилка в faker:", e)

