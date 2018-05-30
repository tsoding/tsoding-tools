{-|
- Use `generateCsvScheduleThisMonth` or `generateCsvScheduleNextMonth` to generate a CSV file.
- Open Google Calendar on a computer. Note: You can only import from a computer, not a phone or tablet.
- In the top right, click Settings
- Open the Calendars tab.
- Click Import calendar between the "My calendars" and "Other Calendars" sections.
- Click Choose File and select the file you exported. The file should end in "ics" or "csv"
- Choose which calendar to add the imported events to. By default, events will be imported into your primary calendar.
- Click Import.
- More info on https://support.google.com/calendar/answer/37118?hl=en
-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TypeSynonymInstances #-}
module Schedule.Core where

import qualified Data.ByteString.Lazy as BS
import           Data.Csv
import qualified Data.Set as S
import           Data.String
import           Data.Time
import           Data.Time.Calendar
import           Data.Time.Calendar.WeekDate
import qualified Data.Vector as V
import           Text.Printf

type Date = Day
type Time = DiffTime

data WeekDay = Mon | Tue | Wed
             | Thu | Fri | Sat
             | Sun
               deriving (Show, Eq, Ord, Enum)

data Project = Project { projectName :: String
                       , projectDescription :: String
                       , projectDays :: S.Set WeekDay
                       , projectTime :: Time
                       }

data Event = Event { eventDescription :: String
                   , eventStartDate :: Date
                   , eventStartTime :: Time
                   , eventSubject :: String
                   } deriving Show

instance ToField Time where
    toField t = fromString $ printf "%02d:%02d" h m
        where h = (it `div` 60) `div` 60
              m = (it `div` 60) `mod` 60
              it = round t :: Int

instance ToField Date where
    toField dt = fromString $ printf "%02d/%02d/%d" d m y
        where (y, m, d) = toGregorian dt

instance ToNamedRecord Event where
    toNamedRecord e =
        namedRecord [ "Description" .= eventDescription e
                    , "Start date"  .= eventStartDate e
                    , "Start time"  .= eventStartTime e
                    , "Subject"     .= eventSubject e
                    ]

type Recipe = [Project]
type Schedule = [Event]

recipe :: Recipe
recipe = [ Project { projectName = "YouTube Content or whatever"
                   , projectDescription = "YouTube Content or whatever"
                   , projectDays = S.fromList [ Tue ]
                   , projectTime = mkTime 22 0
                   }
         , Project { projectName = "Bot in Haskell"
                   , projectDescription = "https://github.com/tsoding/hypernerd"
                   , projectDays = S.fromList [ Thu ]
                   , projectTime = mkTime 22 0
                   }
         , Project { projectName = "Platformer Game in Pure C"
                   , projectDescription = "https://github.com/tsoding/nothing"
                   , projectDays = S.fromList [ Sat, Sun ]
                   , projectTime = mkTime 22 0
                   }
         ]

mkTime :: Integer -> Integer -> Time
mkTime h m = secondsToDiffTime (h * 60 * 60 + m * 60)

datesOfMonth :: Date -> [Date]
datesOfMonth dt = map (\d1 -> fromGregorian y m d1) $ [1 .. gregorianMonthLength y m]
    where (y, m, d) = toGregorian dt

dayOfDate :: Date -> WeekDay
dayOfDate d = enumFromTo Mon Sun !! (dayNumber - 1)
    where (_, _, dayNumber) = toWeekDate d

scheduleProjectForDate :: Date -> Project -> [Event]
scheduleProjectForDate d p
    | dayOfDate d `S.member` projectDays p =
        return Event { eventDescription = projectDescription p
                     , eventStartDate = d
                     , eventStartTime = projectTime p
                     , eventSubject = projectName p
                     }
    | otherwise = []

scheduleRecipeForDate :: Recipe -> Date -> [Event]
scheduleRecipeForDate r d = concatMap (scheduleProjectForDate d) r

scheduleRecipeForMonth :: Recipe -> Date -> Schedule
scheduleRecipeForMonth r = concatMap (scheduleRecipeForDate r) . datesOfMonth

generateCsvScheduleForMonth :: FilePath -> Date -> IO ()
generateCsvScheduleForMonth filePath dt =
    BS.writeFile filePath
      $ encodeByName (V.fromList [ "Description"
                                 , "Start date"
                                 , "Start time"
                                 , "Subject"
                                 ])
      $ scheduleRecipeForMonth recipe dt

generateCsvScheduleThisMonth :: FilePath -> IO ()
generateCsvScheduleThisMonth filePath =
    utctDay <$> getCurrentTime >>= generateCsvScheduleForMonth filePath

generateCsvScheduleNextMonth :: FilePath -> IO ()
generateCsvScheduleNextMonth filePath =
    addGregorianMonthsClip 1 . utctDay <$> getCurrentTime >>= generateCsvScheduleForMonth filePath
