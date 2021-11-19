from selenium import webdriver
import selenium.common.exceptions as selenium_exceptions

homepage = 'http://nebo.mobi/'
image_prefix = '/images/icons/tb_'
image_postfix = '.png'

manage_dict = {}

def pause(reason:str = None):
    a = input(f'Pause: {reason}')

def await_load(load_action):
    print('Loading page')

    load_action()
    while True:
        try:
            end_load_element = page.find_element('css selector', '.main>.cntr>span>img')
            page.execute_script('arguments[0].getAttribute("src")', end_load_element)
            break

        except selenium_exceptions.NoSuchElementException:
            continue

    print('Loaded')

page = webdriver.Firefox()
page.get(homepage+'login')
pause('Awaiting user')

login_form = page.find_element('css selector', '.main>div>.cntr>.nfl>div>form')
inputs = login_form.find_elements('css selector', 'label>input')
login_button = login_form.find_element('css selector', 'input')

page.execute_script('arguments[0].setAttribute("value", "Whu")', inputs[0])
page.execute_script('arguments[0].setAttribute("value", "20portal13")', inputs[1])

await_load(login_button.submit)

while True:
    manage_button = page.find_element('css selector', '.main>.tlbr>[href*="floors"]')

    manage_action_image = manage_button.find_element('css selector', 'img')
    image_name = page.execute_script('return arguments[0].getAttribute("src")', manage_action_image)
    manage_action = image_name.replace(image_prefix, '').replace(image_postfix, '')

    try:
        amount = int(manage_button.find_element('css selector', 'span>span').text)
        await_load(manage_button.click)

    except selenium_exceptions.NoSuchElementException:
        print('Managment completed')

    print(manage_action)
    
    if manage_action == 'empty':
         while amount != 0:
            floor = page.find_element('css selector', '.main>div>ul>li')
            action_button = floor.find_element('css selector', 'div>.flbdy>.flst>span>a')
            await_load(action_button.click)

            buy_buttons = page.find_elements('css selector', '.main>div>div>.prd>li')
            for button in reversed(buy_buttons):
                try:
                    action_button = button.find_element('css selector', '.prdst>.action>.tdu')
                    await_load(action_button.click)

                except selenium_exceptions.NoSuchElementException:
                    print('Goods is stocking')

                except selenium_exceptions.StaleElementReferenceException:
                    break
                        
            amount -= 1
        
    elif (manage_action == 'stocked') or (manage_action == 'sold'):
        while amount != 0:
            floor = page.find_element('css selector', '.main>div>ul>li')
            action_button = floor.find_element('css selector', 'div>div>.flst>span>a')
            await_load(action_button.click)

            amount -= 1

    elif manage_action == 'stocking':
        lift_button = page.find_element('css selector', '.main>.tlbr>.tdn')
        await_load(lift_button.click)
        
        while True:
            try:
                action_button = page.find_element('css selector', '.main>div>.lift>.ctrl>.tdu')
                await_load(action_button.click)
                
            except selenium_exceptions.NoSuchElementException:
                print('Routine completed')
                pause('Awaiting user')
                page.quit()
                exit()
