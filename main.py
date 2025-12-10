from fastapi import FastAPI, HTTPException
from app.schemas.product import ProductItem, ProductCreate
from app.services.products_service import list_products_with_time
from app.repositories.products_repo import insert_product, update_product

app = FastAPI(title="Продукция мебельной компании")

@app.get("/products", response_model=list[ProductItem])
def get_products():
    return list_products_with_time()

@app.post("/products")
def create_product(product: ProductCreate):
    product_id = insert_product(product.dict())
    return {"id": product_id, "message": "Product created successfully"}

@app.put("/products/{product_id}")
def edit_product(product_id: int, product: ProductCreate):
    update_product(product_id, product.dict())
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def remove_product(product_id: int):
    delete_product(product_id)
    return {"message": "Product deleted successfully"}