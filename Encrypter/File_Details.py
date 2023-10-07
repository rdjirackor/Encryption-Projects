import datetime
def file_details():
    Author="Blank"
    Date_Raw=datetime.datetime.now()
    Time=Date_Raw.strftime("%d_%B_%Y_%H_%M_%S")
    added_details=Author+"_"+Time
    return added_details