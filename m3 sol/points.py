def batting_points(runs,balls,fields,fours,sixes):
    pt=runs/2
    if runs>=50:
        pt=pt+5
    if runs>=100:
        pt=pt+10
    sr=runs/balls
    if sr>=0.8 and sr<=1.0:
        pt=pt+2
    if sr>=1.0:
        pt=pt+4
    pt=pt+(1*fours)+(2*sixes)
    pt=pt+(10*fields)
    return int(pt)
  

def bowling_points(wkt,runs,over):
    pt=10*wkt
    if wkt>=3:
        pt=pt+5
    if wkt>=5:
        pt=pt+10
    er=runs/over
    if er>3.5 and er<=4.5:
        pt=pt+4
    elif er>=2 and er<=3.5:
        pt=pt+7
    elif er<2:
        pt=pt+10
    return pt


        
    
    
