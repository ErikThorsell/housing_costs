# Housing Costs

The plan is to fill this repository with small tools that can be useful when making mortgage related calculations.
The tools are written with the **Swedish** market and laws in mind.

## Installation

* [Install Poetry](https://python-poetry.org/docs/#installation)
* Run `poetry install`
* Look at the usage for the tool you want to use.

## Tools

### Amortization Calculation

Usage:

```
python src/amortization_calculator/main.py --monthly-income 60000 --house-price 5000000 --down-payment 1000000 --interest 2.5
```

You can specify `--stop-amortizing` if you want to stop amortizing when you're allowed to and you can
specify a `--minimum-amortization` if you want to put a floor on your amortization amount.

**Note:** Amortization is re-calculated yearly.