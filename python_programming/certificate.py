test_settings = {'theme': 'light'}

def add_setting(test_settings,sample_tuple):
   
    key,value = sample_tuple
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    if not key in test_settings:
        test_settings[key]= value
        return f"Setting '{key}' added with value '{value}' successfully!"

add_setting({'theme': 'light'}, ('volume', 'high'))

def update_setting(test_settings,sample_tuple):
    key,value = sample_tuple
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    if not key in test_settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(test_settings,sample_tuple):
    key = sample_tuple
    key= key.lower()
    if key in test_settings:
        test_settings.pop(key)
        return "Setting 'theme' deleted successfully!" 
    if not key in test_settings:
        return 'Setting not found!'
def view_settings(test_settings):
    
    if not test_settings:
        return 'No settings available.'
    if test_settings:
        result =''
        for key,value in test_settings.items():
            result += f'{key.capitalize()}:{value}\n'
        return result
        