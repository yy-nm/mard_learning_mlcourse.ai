
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# we don't like warnings
# you can comment the following 2 lines if you'd like to
import warnings
warnings.filterwarnings('ignore')


data_path = "2008.csv"
#data_path = "2008.csv.bz2"

dtype = {'DayOfWeek': np.uint8, 'DayofMonth': np.uint8, 'Month': np.uint8 , 'Cancelled': np.uint8,
		 'Year': np.uint16, 'FlightNum': np.uint16 , 'Distance': np.uint16,
		 'UniqueCarrier': str, 'CancellationCode': str, 'Origin': str, 'Dest': str,
		 'ArrDelay': np.float16, 'DepDelay': np.float16, 'CarrierDelay': np.float16,
		 'WeatherDelay': np.float16, 'NASDelay': np.float16, 'SecurityDelay': np.float16,
		 'LateAircraftDelay': np.float16, 'DepTime': np.float16}

raw_data = pandas.read_csv(data_path, usecols=dtype.keys(), dtype=dtype)

# print(raw_data.info())
#print(raw_data.dtypes)
#print(raw_data.columns)
# print(raw_data.head())


### answer 1
print("answer 1")
# carrier_data = raw_data['UniqueCarrier']
# print(carrier_data.nunique())
print(raw_data.groupby('UniqueCarrier').size().sort_values(ascending=False).head(10))
# print(raw_data.groupby('UniqueCarrier').size().head(10))


### answer 2
print("answer 2")
# print(raw_data['UniqueCarrier'].nunique())
print(raw_data.groupby('CancellationCode').size().sort_values(ascending=False).head(10))


### answer 3
print("answer 3")
print(raw_data.groupby(['Origin', 'Dest']).size().sort_values(ascending=False).head(10))


### answer 4
print("answer 4")
delay_data = raw_data[raw_data['DepDelay'] > 0 & (not raw_data['DepDelay'].isna)]
delay_top5_route = delay_data.groupby(['Origin', 'Dest'])['DepDelay'].size().sort_values(ascending=False).head(5)
print(delay_data.groupby(['Origin', 'Dest'])['DepDelay'].size().sort_values(ascending=False).head(5))
# print(delay_top5_route.shape)
# print(delay_top5_route.keys())
# print(delay_top5_route.items())
#for name in delay_top5_route:
#	print(name)
#	pass

delay_top5_route_origin = ['LAX', 'DAL', 'SFO', 'ORD', 'HOU']
delay_top5_route_dest = ['SFO', 'HOU', 'LAX', 'LGA', 'DAL']

wether_delay_count = 0
for i in range(len(delay_top5_route_origin)):
	wether_delay_count += len(raw_data[(raw_data['WeatherDelay'] > 0) & (raw_data['Origin'] == delay_top5_route_origin[i]) & (raw_data['Dest'] == delay_top5_route_dest[i])])
	pass

print(wether_delay_count)


### answer 5
print("answer 5")
### answer 5
fig_data = raw_data[~raw_data['DepTime'].isna()]
sns.distplot(fig_data['DepTime'])


### answer 6
print("answer 6")
print(raw_data.groupby('Month').size().sort_values(ascending=False))
print(raw_data.groupby('DayOfWeek').size().sort_values(ascending=False))


### answer 7
print("answer 7")
# A: carrier
# B: weather condition
# C: national air system
# D: security reasions
print(raw_data.groupby(['Month', 'CancellationCode']).size().sort_values(ascending=False))
print(raw_data.groupby(['CancellationCode']).size().sort_values(ascending=False))


### answer 8
print("answer 8")
# print(raw_data[raw_data['Cancelled'] > 0].groupby('Month').size().sort_values(ascending=False))
print(raw_data[raw_data['CancellationCode'] == 'A'].groupby('Month').size().sort_values(ascending=False).head(1))


### answer 9
print("answer 9")
print(raw_data[(raw_data['CancellationCode'] == 'A') & (raw_data['Month'] == 4)].groupby('UniqueCarrier').size().sort_values(ascending=False).head(1))


### answer 10
print("answer 10")
print(raw_data[~raw_data['ArrDelay'].isna()].groupby('UniqueCarrier')['ArrDelay'].median().sort_values(ascending=True))
print(raw_data[~raw_data['DepDelay'].isna()].groupby('UniqueCarrier')['DepDelay'].median().sort_values(ascending=True))

