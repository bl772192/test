if __name__ == "__main__":
    
    import Connect
    import os
    import sys

    Input = Connect.Input()#
    Stellwerte_In=['Value1','Value2','Value3','Value4','Value5','Value6','Value7','Value8',9111111111,9,9,111,111,111,999,666]
    Get_result_In = Input.save_to_rest(Stellwerte_In)#
    if Get_result_In == 201: #
        print "Successful Post"#

"""
    Output = Connect.Output()#
    #Stellwerte_Out=[];
    Get_result_Out = Output.get_from_rest()#
    if Get_result_Out == 200: #
        print "Successful Get"#
"""