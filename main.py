from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

energy_data = [120, 135, 150, 140, 170, 165, 180, 175, 160, 190]


class EnergyInput(BaseModel):
    value: int


@app.get("/")
def home():
    return {"message": "Energy API is running"}


@app.get("/energy")
def get_energy():
    return {"energy_production": energy_data}


@app.get("/average")
def get_average():
    average = sum(energy_data) / len(energy_data)
    return {"average_energy": average}


@app.get("/max")
def get_max():
    maximum = max(energy_data)
    return {"max_energy": maximum}


@app.get("/min")
def get_min():
    minimum = min(energy_data)
    return {"min_energy": minimum}


@app.get("/summary")
def get_summary():
    average = sum(energy_data) / len(energy_data)
    maximum = max(energy_data)
    minimum = min(energy_data)
    count = len(energy_data)

    return {
        "average_energy": average,
        "max_energy": maximum,
        "min_energy": minimum,
        "count": count
    }


@app.post("/add-energy")
def add_energy(new_energy: EnergyInput):
    energy_data.append(new_energy.value)
    return {
        "message": "New energy value added successfully",
        "updated_energy_data": energy_data
    }