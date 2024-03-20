from fastapi import FastAPI

ITEMS = {
    "0": "RAM",
    "1": "CPU",
    "2": "HDD",
    "3": "SDD",
    "4": "NIC",
    "5": "FDD",
    "6": "DVD",
    "7": "CDROM",
    "8": "USB",
    "9": "HDMI",
    "10": "VDI",
    "11": "PCI"
}

app = FastAPI()

@app.get("/")
async def root():
    return 'Hello World!'


@app.get("/items")
async def items():
    return ITEMS


@app.get("/item/{item_id}")
async def item(item_id):
    try:
        record = ITEMS[item_id]
    except:
        record = []
    return record
