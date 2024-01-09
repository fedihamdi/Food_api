
import requests

class OpenFoodFact:
    url= ""
    def get_product_by_code(self, bar_code):
        try:
            response = requests.get(url = self.url + "/api/v0/product/" + bar_code + ".json")
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise err
        return response.json()

open_food_fact = OpenFoodFact()

def setup_open_food_fact(app):
    open_food_fact.url = app.config["OPEN_FOOD_FACT_URL"]