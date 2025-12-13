import time
""" External library code """

class ExternalService:
  def fetchData(self):
    print("Starting slow network call.")
    time.sleep(5)
    return "Real data from server."
API_service = ExternalService()   
 
"""End of External library code """

def run_original_call():
  start_time = time.time()
  result = API_service.fetchData()
  endTime = time.time()
  print("Result: ", result)
  print("Time Taken: {}".format(endTime-start_time))

def mock_fetch_data():
  print('Mocked --  ByPassing network Call')
  return 'Mocked test data'
  
def run_patched_call():
  API_service.fetchData = mock_fetch_data   # monkey Patching
  start_time = time.time()
  result = API_service.fetchData()
  endTime = time.time()
  print("Result: ", result)
  print("Time Taken: {}".format(endTime-start_time))
      
if __name__=='__main__':
  #  run_original_call()
  run_patched_call()