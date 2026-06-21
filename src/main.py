from farmer.menu import Menu
from farmer import diagnostics
from farmer import functions

def main():
    main_menu =[
        "Check layout",
        "Check color",
        "Show info",
        "test automation start"
    ]

    actions = [
        diagnostics.check_layout,
        diagnostics.check_buildings,
        diagnostics.show_info,
        functions.start_production

    ]

    while True:
        answer = Menu.show(main_menu)
        if answer is None:
            break
        actions[answer]()

if __name__ == "__main__":
    main()


