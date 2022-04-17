from pydantic import BaseModel, root_validator


class City(BaseModel):
    city_name: str
    lat: float
    lon: float
    country: str


class CityWeatherData(BaseModel):
    city_name: str
    country: str
    min: float
    max: float
    feels_like: float

    @root_validator
    def calculate_avg_temperature(cls, values):
        values["avg"] = round((values.get("min") + values.get("max")) / 2, 2)
        return values
