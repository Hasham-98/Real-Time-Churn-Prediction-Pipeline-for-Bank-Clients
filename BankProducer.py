from kafka import KafkaProducer
import csv
import time
import json

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Convert data to JSON format
)

# Define the CSV file to read
csv_file = '/home/wick/Templates/vscodes/kafka/Churn_Modelling.csv'

# Function to read CSV and stream to Kafka in batches of 1000 rows
def stream_csv_to_kafka(batch_size=1000, delay_between_batches=180):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)  # Read CSV rows as dictionaries
        buffer = []
        
        for row in reader:
            buffer.append(row)
            
            # If buffer reaches batch_size, send the batch to Kafka
            if len(buffer) == batch_size:
                producer.send('streamig-bank-data', value=buffer)
                print(f"Sent batch of {batch_size} rows to Kafka")
                buffer.clear()  # Clear buffer after sending

                # Simulate delay between batches (in seconds)
                time.sleep(delay_between_batches)
        
        # Send remaining rows if buffer is not empty
        if buffer:
            producer.send('streamig-bank-data', value=buffer)
            print(f"Sent final batch of {len(buffer)} rows to Kafka")

    producer.flush()

# Stream the data to Kafka
if __name__ == "__main__":
    stream_csv_to_kafka()


