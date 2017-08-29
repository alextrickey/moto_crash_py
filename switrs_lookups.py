#SWITRS Lookups

collision_severity = {
    '1' = 'Fatal',
    '2' = 'Injury (Severe)',
    '3' = 'Injury (Other Visible)',
    '4' = 'Injury (Complaint of Pain)',
    '0' = 'PDO (property damage only)'
    }

weekday = {
    '1'='M',
    '2'='Tu',
    '3'='W',
    '4'='Th',
    '5'='F',
    '6'='Sa',
    '7'='Su'
    }

violation = {
    '01' = 'Driving or Bicycling Under the Influence of Alcohol or Drug',
    '02' = 'Impeding Traffic',
    '03' = 'Unsafe Speed',
    '04' = 'Miscellaneous', #'Following Too Closely' -- only 5 cases
    '05' = 'Wrong Side of Road',
    '06' = 'Improper Passing',
    '07' = 'Unsafe Lane Change',
    '08' = 'Improper Turning',
    '09' = 'Automobile Right of Way',
    '10' = 'Pedestrian Right of Way',
    '11' = 'Pedestrian Violation',
    '12' = 'Traffic Signals and Signs',
    '13' = 'Hazardous Parking',
    '14' = 'Lights',
    '15' = 'Miscellaneous', #'Brakes' -- only 1 case
    '16' = 'Miscellaneous', #'Other Equipment' -- only 1 case
    '17' = 'Other Hazardous Violation',
    '18' = 'Other Than Driver (or Pedestrian)',
    '19' = 'Code 19', #Not documented
    '20' = 'Code 20', #Not documented
    '21' = 'Unsafe Starting or Backing',
    '22' = 'Other Improper Driving',
    '23' = 'Pedestrian or "Other" Under the Influence of Alcohol or Drug',
    '24' = 'Fell Asleep',
    '00' = 'Unknown'
    }

weather = {
  'weather_clear'  = 'A',
  'weather_cloudy' = 'B',
  'weather_rainy'  = 'C',
  'weather_snowy'  = 'D',
  'weather_foggy'  = 'E',
  'weather_other'  = 'F',
  'weather_windy'  = 'G'
  }

collision_type = {
  'A' = 'Head-On',
  'B' = 'Sideswipe',
  'C' = 'Rear End',
  'D' = 'Broadside',
  'E' = 'Hit Object',
  'F' = 'Overturned',
  'G' = 'Vehicle/Pedestrian',
  'H' = 'Other'
  }

control_device = {
  'A' = 'Functioning',
  'B' = 'Not Functioning',
  'C' = 'Obscured',
  'D' = 'None'
  }

mviw_ = {
  'A' = 'Non-Collision',
  'B' = 'Pedestrian',
  'C' = 'Other Motor Vehicle',
  'D' = 'Motor Vehicle on Other Roadway',
  'E' = 'Parked Motor Vehicle',
  'F' = 'Train',
  'G' = 'Bicycle',
  'H' = 'Animal',
  'I' = 'Fixed Object',
  'J' = 'Other Object'
  }

road_surface = {
  'A' = 'Dry',
  'B' = 'Wet',
  'C' = 'Snowy or Icy',
  'D' = 'Slippery (Muddy, Oily, etc.)'
  }

lighting = {
  'A' = 'Daylight',
  'B' = 'Dusk or Dawn',
  'C' = 'Dark - Street Lights',
  'D' = 'Dark - No Street Lights',
  'E' = 'Dark - No Street Lights'
  #E='Dark - Street Lights Not Functioning' very rare
  #combining with code D
  }
