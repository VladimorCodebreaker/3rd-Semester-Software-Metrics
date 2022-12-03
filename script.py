"""############## Performance Measurement Tool | Assignment 2 ##############"""
import pprint
from collections import defaultdict
from selenium import webdriver


dict = defaultdict(list)


def get_metrics():
    """Get Web-Console Performance Data"""
    print("Getting performance data...")
    driver = webdriver.Safari()
    driver.get("https://en.wikipedia.org/wiki/Software_metric")
    query = "return window.performance.getEntries();"
    result = driver.execute_script(query)
    driver.quit()
    prettifier = pprint.PrettyPrinter(indent=4)

    for element in result:
        dict[element["name"]].append(element["duration"])


def calc_average():
    """Calculate the average duration"""
    for key, value in dict.items():
        dict[key] = sum(value) / float(len(value))


def write_to_file():
    """Write to a CSV file"""
    with open("result.csv", "w", encoding="utf-8") as file:
        file.write("Name, Duration\n\n")
        for key, value in dict.items():
            file.write(f"{key}, {str(value)}\n")


if __name__ == "__main__":
    for _ in range(10):
        get_metrics()
    calc_average()
    write_to_file()
