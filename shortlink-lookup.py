import requests
from urllib.parse import urlparse

def resolve_shortlink(shortlink):
    try:
        response = requests.head(shortlink, allow_redirects=True)
        final_url = response.url
        return final_url
    except requests.exceptions.RequestException:
        return None

def main():
    input_file = "shortlinks.txt"
    output_file = "results.txt"

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        shortlinks = f_in.read().splitlines()

        for shortlink in shortlinks:
            actual_url = resolve_shortlink(shortlink)

            if actual_url:
                f_out.write(f"Shortlink: {shortlink}\n")
                f_out.write(f"URL sebenarnya: {actual_url}\n\n")
            else:
                f_out.write(f"Shortlink: {shortlink}\n")
                f_out.write("Tidak dapat menemukan URL sebenarnya.\n\n")

if __name__ == "__main__":
    main()