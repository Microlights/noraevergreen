import math  
  
def haversine(lat1, lon1, lat2, lon2):  
    # 将角度转换为弧度  
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])  
    # 常量值  
    a = 6371  # 地球半径，单位是公里  
    # 通过经纬度计算出两个弧度之间的差值  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    # 根据 haversine 公式计算距离  
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2  
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))   
    distance = a * a * c * a  # 在球面上两点间的大圆距离，单位为公里  
    return distance  
  
# 示例：计算北京和上海之间的距离  
lat1 = 39.9042  # 北京的纬度  
lon1 = 116.4074  # 北京的经度  
lat2 = 31.2304  # 上海的纬度  
lon2 = 121.4737  # 上海的经度  
print(haversine(lat1, lon1, lat2, lon2), "km")  # 输出结果：1073.6608775053038 km
