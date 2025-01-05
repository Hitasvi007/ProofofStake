import hashlib
import random
import time

class Block:
    def __init__(self, data, previous_hash, validator):
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.validator = validator  
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = str(self.timestamp) + str(self.data) + str(self.validator) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.stakes = {}  
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("Genesis Block", "0", "Genesis Node")
        self.chain.append(genesis_block)

    def add_participant(self, participant, stake):

        self.stakes[participant] = stake

    def select_validator(self):
        
        total_stake = sum(self.stakes.values())
        if total_stake == 0:
            return None
        
        chosen = random.choices(list(self.stakes.keys()), weights=self.stakes.values())[0]
        return chosen

    def add_block(self, data):
        validator = self.select_validator() 
        if not validator:
            print("No valid participants to validate the block.")
            return
        previous_hash = self.chain[-1].hash  
        new_block = Block(data, previous_hash, validator)  
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {self.chain.index(block)}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Validator: {block.validator}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}\n")

if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Add participants and their stake
    my_blockchain.add_participant("Validator_A", 50)  
    my_blockchain.add_participant("Validator_B", 30)  
    my_blockchain.add_participant("Validator_C", 20)  

    # Add blocks to the blockchain
    my_blockchain.add_block({
        "sensor_id": "WeatherStation_01",
        "location": "City_Park",
        "readings": {
            "temperature": 18.3,  
            "humidity": 70.4,     
            "wind_speed": 12.8,   
            "rainfall": 5.2      
        }
    })

    my_blockchain.add_block({
        "sensor_id": "AirMonitor_X5",
        "location": "Downtown",
        "readings": {
            "CO2": 400,           
            "PM2.5": 35,          
            "PM10": 50,          
            "Ozone": 0.07         
        }
    })

    my_blockchain.add_block({
        "sensor_id": "Machine_23",
        "location": "Factory_Floor_2",
        "readings": {
            "vibration": 0.3,     
            "temperature": 75.0,  
            "noise_level": 85,    
            "operating_hours": 120 
        }
    })

    my_blockchain.add_block({
        "sensor_id": "WaterSensor_Lake_1",
        "location": "Lake_Reservoir",
        "readings": {
            "pH": 7.4,           
            "dissolved_oxygen": 6.8, 
            "turbidity": 2.3,     
            "conductivity": 150   
        }
    })

    my_blockchain.add_block({
        "sensor_id": "SoilMoisture_12",
        "location": "Farm_Field_4",
        "readings": {
            "soil_moisture": 32.5, 
            "soil_temperature": 19.7, 
            "nitrogen_level": 15,  
            "phosphorus_level": 10 
        }
    })

    my_blockchain.display_chain()

    print("Is Blockchain Valid?", my_blockchain.is_chain_valid())
