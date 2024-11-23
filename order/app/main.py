# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pika

# app = FastAPI()

# # Model untuk pesanan
# class Order(BaseModel):
#     user_id: int 
#     items: dict  # Format: {"sepatu": 2, "baju": 3}

# # Koneksi RabbitMQ
# # rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
# rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('myuser', 'mypassword')))
# channel = rabbitmq_connection.channel()
# channel.queue_declare(queue="orders_queue")

# @app.get("/")
# def read_root():
#     return {"message": "API is running"}


# @app.post("/orders")
# def create_order(order: Order):
#     try:
#         # Kirim pesan ke RabbitMQ
#         channel.basic_publish(
#             exchange="",
#             routing_key="orders_queue",
#             body=str(order.model_dump())  # Serialisasi data menjadi string
#         )
#         return {"message": "Order has been sent to RabbitMQ", "order": order}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to process order: {e}")



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pika
import time

app = FastAPI()

# Model untuk pesanan
class Order(BaseModel):
    user_id: int
    items: dict

# Global RabbitMQ connection
rabbitmq_connection = None
channel = None

# Fungsi untuk membuat koneksi RabbitMQ dengan mekanisme retry
def connect_to_rabbitmq():
    global rabbitmq_connection, channel
    while True:
        try:
            print("Connecting to RabbitMQ...")
            rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
            # rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('myuser', 'mypassword')))

            channel = rabbitmq_connection.channel()
            channel.queue_declare(queue="orders_queue")
            print("Connected to RabbitMQ.")
            break
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Connection to RabbitMQ failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

# Panggil fungsi koneksi saat aplikasi dimulai
connect_to_rabbitmq()

@app.post("/orders")
def create_order(order: Order):
    global channel
    try:
        if channel is None or channel.is_closed:
            print("RabbitMQ channel is closed. Reconnecting...")
            connect_to_rabbitmq()

        # Kirim pesan ke RabbitMQ
        channel.basic_publish(
            exchange="",
            routing_key="orders_queue",
            body=str(order.dict())
        )
        return {"message": "Order has been sent to RabbitMQ", "order": order}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process order: {e}")
