import utils
import os


def download():
    print("[!] Downloading Datasets")
    utils.downloader("https://www.trentinotrasporti.it/opendata/google_transit_extraurbano_tte.zip", "web/txt_datasets/")
    utils.downloader("https://www.trentinotrasporti.it/opendata/google_transit_urbano_tte.zip", "web/txt_datasets/")
    print("[!] Downloaded Datasets")


def convert():
    print("[!] Converting Dataset from txt to json")
    # Extraurban Dataset
    utils.csvtojson("web/txt_datasets/Suburban/agency.txt", "web/json_datasets/Suburban/agency.json")
    utils.csvtojson("web/txt_datasets/Suburban/calendar.txt", "web/json_datasets/Suburban/calendar.json")
    utils.csvtojson("web/txt_datasets/Suburban/calendar_dates.txt", "web/json_datasets/Suburban/calendar_dates.json")
    utils.csvtojson("web/txt_datasets/Suburban/feed_info.txt", "web/json_datasets/Suburban/feed_info.json")
    utils.csvtojson("web/txt_datasets/Suburban/routes.txt", "web/json_datasets/Suburban/routes.json")
    utils.csvtojson("web/txt_datasets/Suburban/shapes.txt", "web/json_datasets/Suburban/shapes.json")
    utils.csvtojson("web/txt_datasets/Suburban/stop_times.txt", "web/json_datasets/Suburban/stop_times.json")
    utils.csvtojson("web/txt_datasets/Suburban/stops.txt", "web/json_datasets/Suburban/stops.json")
    utils.csvtojson("web/txt_datasets/Suburban/stopslevel.txt", "web/json_datasets/Suburban/stopslevel.json")
    utils.csvtojson("web/txt_datasets/Suburban/transfers.txt", "web/json_datasets/Suburban/transfers.json")
    utils.csvtojson("web/txt_datasets/Suburban/trips.txt", "web/json_datasets/Suburban/trips.json")

    # Urban Dataset
    utils.csvtojson("web/txt_datasets/Urban/agency.txt", "web/json_datasets/Urban/agency.json")
    utils.csvtojson("web/txt_datasets/Urban/calendar.txt", "web/json_datasets/Urban/calendar.json")
    utils.csvtojson("web/txt_datasets/Urban/calendar_dates.txt", "web/json_datasets/Urban/calendar_dates.json")
    utils.csvtojson("web/txt_datasets/Urban/feed_info.txt", "web/json_datasets/Urban/feed_info.json")
    utils.csvtojson("web/txt_datasets/Urban/routes.txt", "web/json_datasets/Urban/routes.json")
    utils.csvtojson("web/txt_datasets/Urban/shapes.txt", "web/json_datasets/Urban/shapes.json")
    utils.csvtojson("web/txt_datasets/Urban/stop_times.txt", "web/json_datasets/Urban/stop_times.json")
    utils.csvtojson("web/txt_datasets/Urban/stops.txt", "web/json_datasets/Urban/stops.json")
    utils.csvtojson("web/txt_datasets/Urban/stopslevel.txt", "web/json_datasets/Urban/stopslevel.json")
    utils.csvtojson("web/txt_datasets/Urban/transfers.txt", "web/json_datasets/Urban/transfers.json")
    utils.csvtojson("web/txt_datasets/Urban/trips.txt", "web/json_datasets/Urban/trips.json")


def extract():
    utils.extractor("web/txt_datasets/google_transit_extraurbano_tte.zip", "web/txt_datasets/Suburban")
    utils.extractor("web/txt_datasets/google_transit_urbano_tte.zip", "web/txt_datasets/Urban")
    os.remove("web/txt_datasets/google_transit_urbano_tte.zip")
    os.remove("web/txt_datasets/google_transit_extraurbano_tte.zip")

if __name__ == "__main__":
    utils.cleanup()
    utils.init()
    download()
    extract()
    convert()
