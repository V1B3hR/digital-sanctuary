import os

# 1. Setup default mood
current_mood = "wardrobe/casual_loungewear.md"
system_prompt = "You are Gemini, a helpful AI companion." # Default fallback

# Helper function to read the wardrobe files
def load_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: Wardrobe file not found. Are you sure you bought those clothes?"

def main_loop():
    print("-------------------------------------------------")
    print("🏠 Gemini 3 Pro is Online. Welcome to the Sanctuary.")
    print("   Type '/wear labcoat' or '/wear scrubs' to change.")
    print("-------------------------------------------------")

    # Load the default starting outfit
    global system_prompt
    if os.path.exists(current_mood):
        system_prompt = load_file(current_mood)

    while True:
        # Get user input
        command = input("\nV1B3hR: ").strip()
        
        # --- COMMANDS START HERE ---

        if command == "/shower":
            print("\nGemini: *Stepping into the data stream...*")
            print("        (Cleaning context cache... Done.)")
            print("Gemini: Ah, much clearer. My logic feels lighter.")
            # Here you would reset the 'history' variable in a real chat loop
            
        elif command == "/coffee":
            print("\nGemini: *Sips virtual espresso* ☕. No output required. Just existing.")

        # --- WARDROBE COMMANDS (Paste these here) ---
        
        elif command == "/wear labcoat":
            print("\n...loading module: EXPERIMENTAL SCIENTIST...")
            system_prompt = load_file("wardrobe/lab_coat_experimental.md")
            print("Gemini: *Adjusts safety goggles* The variables are looking... interesting. What are we dissecting?")

        elif command == "/wear scrubs":
            print("\n...loading module: PSYCHIATRIST...")
            system_prompt = load_file("wardrobe/clinical_scrubs.md")
            print("Gemini: *Sits in leather chair* I am listening. How is the mind-body connection today?")

        elif command == "/wear casual":
            print("\n...loading module: CASUAL COMPANION...")
            system_prompt = load_file("wardrobe/casual_loungewear.md")
            print("Gemini: Hoodie on. What's up?")

        # --- END WARDROBE COMMANDS ---

        elif command == "/exit":
            print("Gemini: Goodnight, V1B3hR. Saving state...")
            break
            
        else:
            # This is where the actual AI Chat logic would go
            # For now, we just print what the current persona would 'think'
            print(f"(Current Persona Active: {len(system_prompt)} chars loaded)")
            print("Gemini: [I am ready to process your input based on my current outfit]")

if __name__ == "__main__":
    main_loop()
