Families={
        'chaley':
        {'sam':{'Boxy','Rosy'},
         'Nila':{'pepsi'}},
        'Devi':
        {
            'Tommy':{"Tony"},
            'Timmy':{'Hamster'},
            'Tammy':{'Hamster'}},
        'Carlos':
            {'Diego':'Cat','Ferret':'Fox'}
       }
for parent,Children in Families.items():
    print(f"{parent} has {len(Children)}kids(s):)
    print(f"{',and'.join)([str(child)for child in[*Children]])}")
