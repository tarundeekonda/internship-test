import pandas as pd

def get2Smallest(arr):
 
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        return arr[0],None;
 
    first = second = 1000000007
    for i in range(0, arr_size):
 
        # If current element is smaller than first then update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]
 
        # If current element is in between first and second then update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]
 
    return first,second

if __name__ == "__main__":

  # Reading filteredCountry.csv into a dataframe
  df = pd.read_csv("filteredCountry.csv")

  # Lists to maintain corresponding SKU, first minimum and second minimum price values 
  SKU = []
  firstMin = []
  secondMin = []

  for each in df.SKU.unique():

    # Get prices associated with current SKU value
    pricedf = df[df['SKU']==each]

    # Get unique price values of current SKU
    prices = pricedf.PRICE.unique()

    # Removing '$',',','?' characters from price value 
    arr = []
    for val in prices:
      val = val.replace('$','')
      val = val.replace(',','')
      val = val.replace('?','')
      arr.append(float(val))

    # Find first and second minimum prices of current SKU
    first, second = get2Smallest(arr)

    # Checking if both first and second minimum exist and only then store the values
    if first is None or second is None:
      continue
    else:
      if first.is_integer():
        first = int(first)
      if second.is_integer():
        second = int(second)
      SKU.append(each)
      firstMin.append(str(first))
      secondMin.append(str(second))
  
  # Converting the above results into a csv
  result = pd.DataFrame({'SKU':SKU,'FIRST_MINIMUM_PRICE':firstMin,'SECOND_MINIMUM_PRICE':secondMin})
  result.to_csv("lowestPrice.csv",index=False)
