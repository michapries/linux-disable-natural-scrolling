import os

def set_scrolling():
    # Put the name of your mouse/touchpad (as it appears in xinput) into this list.
    devices = ['Touchpad', 'ROCCAT ROCCAT Kone Pure Ultra']

    for device in devices:
        # ============================================================
        # Get device ID from xinput.
    
        xinput = os.popen(f'xinput | grep \"{device}\\s*id=\"').read().strip()    
        
        if xinput == '':
            break

        split = xinput.split('\t')

        id = -1

        for elem in split:
            if 'id=' in elem:
                id = elem[3:]

        if id == -1:
            break

        # ============================================================
        # Get natural scrolling ID from list-props.

        list_props = os.popen(f'xinput list-props {id} | grep \"Natural Scrolling Enabled (\" ').read().strip()
        prop = list_props.split(' ')

        prop_id = -1

        for elem in prop:
            if ':' in elem:
                prop_id = elem[1:4]
        
        if prop_id == -1:
            break

        # ============================================================
        # Set natural scrolling to 0.

        os.system(f'xinput set-prop {id} {prop_id} 0')
        print(f'Set natural scrolling for {device} to 0.')
        


if __name__ == '__main__':
    set_scrolling()