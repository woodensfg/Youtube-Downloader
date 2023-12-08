from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL:")

    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    if yd:
        # Download the video to the current directory
        yd.download(r'C:\Users\woodg\Downloads\Youtube Download')
        print("Download complete.")
    else:
        print("No suitable stream found for this video.")

except Exception as e:
    print("An error occurred:", str(e))
