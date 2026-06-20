class Menu:

    @staticmethod
    def show(options):
        print()

        for index, option in enumerate(options):
            print(f"[{index}] {option}")
        
        print("[Q] Quit")

        answer =  input("> ")

        if answer.lower() == "q":
            return None
        
        try:
            index = int(answer)
            if 0 <= index < len(options):
                return index
        except ValueError:
            pass

        print("invalid option.")