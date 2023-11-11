def analyze_metrics(volume_metric, rate_metric):  
    print(f"Volume metric: {volume_metric}")  
    print(f"Rate metric: {rate_metric}")  
      
    if volume_metric >= 1000 and rate_metric >= 100:  
        print("The system is experiencing high demand.")  
    elif volume_metric >= 500 and rate_metric >= 50:  
        print("The system is experiencing medium demand.")  
    elif volume_metric >= 100 and rate_metric >= 10:  
        print("The system is experiencing low demand.")  
    else:  
        print("The system is not experiencing any demand.")  
  
# Example usage  
analyze_metrics(700, 80)
