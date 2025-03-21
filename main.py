from app.execution_engine import CodeEngine

def main():
    engine = CodeEngine()
    print("🤖 Code Execution Agent - GitHub Codespace")
    
    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            code, result = engine.process_command(user_input)
            print(f"\nGenerated Code:\n{code}")
            print(f"\nResult: {result}")
            
    except KeyboardInterrupt:
        print("\nSession saved. Goodbye!")
    except Exception as e:
        print(f"Critical error: {str(e)}")

if __name__ == "__main__":
    main()    