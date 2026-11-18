from ai_engine import generate_commands from deploy_config import deploy
from monitor import monitor
intent = input("Enter network intent: ").lower() # If user wants only monitoring
if "check" in intent:
print("\n[INFO] Monitoring Network Only...") monitor()
else:
commands = generate_commands(intent) print("\nGenerated Commands:\n", commands) print("[INFO] Deploying configuration...") deploy(commands)
print("\n[INFO] Monitoring Network...") monitor()
