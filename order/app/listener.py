# import pika
# import mysql.connector
# import ast  # Untuk parsing string ke dictionary

# db_config = {
#     "host": "mysql",  # Nama layanan di Docker Compose
#     "user": "myuser",
#     "password": "mypassword",
#     "database": "mydatabase",
# }

# # Membuat koneksi ke database MySQL
# connection = mysql.connector.connect(**db_config)

# cursor = connection.cursor()

# # Koneksi ke RabbitMQ
# # rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

# rabbitmq_connection = connect_to_rabbitmq()
# # rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('myuser', 'mypassword')))

# # print("sini")
# channel = rabbitmq_connection.channel()
# channel.queue_declare(queue="orders_queue")
# print("sini 4")

# def connect_to_rabbitmq():
#     for _ in range(5):  # Coba koneksi hingga 5 kali
#         try:
#             connection = pika.BlockingConnection(pika.ConnectionParameters('172.19.0.2', 5672, '/', pika.PlainCredentials('myuser', 'mypassword')))
#             return connection
#         except pika.exceptions.AMQPConnectionError:
#             print("Waiting for RabbitMQ to be ready...")
#             time.sleep(5)
#     raise Exception("Failed to connect to RabbitMQ after multiple attempts.")

# # Daftar harga barang
# def get_price(item_name):
#     cursor.execute("SELECT price FROM prices WHERE item = %s", (item_name,))
#     result = cursor.fetchone()
#     return result[0] if result else 0

# # Callback untuk memproses pesan
# def process_order(ch, method, properties, body):
#     order = ast.literal_eval(body.decode())  # Parse pesan menjadi dictionary
#     user_id = order.get("user_id") 
#     items = order.get("items", {})
    
#     total_price = 0
#     for item, quantity in items.items():
#         price = get_price(item)
#         total_price += price * quantity
#     cursor.execute(
#         "INSERT INTO orders (user_id, items, total_price) VALUES (%s, %s, %s)",
#         (user_id, str(items), total_price)
#     )
#     connection.commit()
    
#     print(f"User ID: {user_id}, Order: {items}, Total Price: {total_price}")

# # Listen ke queue RabbitMQ
# channel.basic_consume(queue="orders_queue", on_message_callback=process_order, auto_ack=True)
# print("Listening for messages...")
# channel.start_consuming()


import pika
import mysql.connector
import ast  # Untuk parsing string ke dictionary

# Koneksi ke MySQL
db_config = {
    "host": "mysql",
    "user": "myuser",
    "password": "mypassword",
    "database": "mydatabase",
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Koneksi ke RabbitMQ
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = rabbitmq_connection.channel()
channel.queue_declare(queue="orders_queue")

# Daftar harga barang
def get_price(item_name):
    cursor.execute("SELECT price FROM prices WHERE item = %s", (item_name,))
    result = cursor.fetchone()
    return result[0] if result else 0

# Callback untuk memproses pesan
def process_order(ch, method, properties, body):
    order = ast.literal_eval(body.decode())  # Parse pesan menjadi dictionary
    user_id = order.get("user_id")           # Ambil user_id
    items = order.get("items", {})
    
    total_price = 0
    for item, quantity in items.items():
        price = get_price(item)
        total_price += price * quantity
    
    # Cetak hasil (bisa disimpan ke DB atau diteruskan ke sistem lain)
    print(f"User ID: {user_id}, Order: {items}, Total Price: {total_price}")

# Listen ke queue RabbitMQ
channel.basic_consume(queue="orders_queue", on_message_callback=process_order, auto_ack=True)
print("Listening for messages...")
channel.start_consuming()
