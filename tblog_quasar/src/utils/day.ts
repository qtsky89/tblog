import dayjs from 'dayjs'

// https://day.js.org/docs/en/display/format#list-of-all-available-formats
export const DATE_FORMAT = {
  YYYYMMDD: 'YYYY-MM-DD',
}

type DayDate = string | number | Date | dayjs.Dayjs | null | undefined

export function formatYYYYMMDD(date: DayDate): string {
  return dayjs(date).format(DATE_FORMAT.YYYYMMDD)
}
