import maya.cmds as cmds
import os
from time import sleep

def save_reminder():
    save_prompt = cmds.confirmDialog(title='Save Reminder', message='Would you like to save your scene?', button=['Yes', 'No', 'Cancel'], defaultButton='Yes', cancelButton='Cancel', dismissString='Cancel')

    if save_prompt == 'Yes':
        save_now = cmds.confirmDialog(title='Save Now?', message='Do you want to save now?', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        if save_now == 'Yes':
            current_scene = cmds.file(q=True, sceneName=True)
            if current_scene:
                save_folder = os.path.dirname(current_scene)
                cmds.file(save=True)
                cmds.warning('Scene saved successfully!')
                cmds.fileBrowserDialog(m='save', fc=save_folder)
            else:
                cmds.warning('Please save the scene before using this option.')
        else:
            cmds.warning('Please remember to save your scene later.')

    elif save_prompt == 'No':
        cmds.warning('Remember to save your work before closing!')
    else:
        cmds.warning('Action cancelled.')

save_reminder()

