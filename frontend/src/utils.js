const getMediaAbsolutePath = (mediaPath) => {
  switch (true) {
    case !mediaPath:
      return "";
    case mediaPath.startsWith("http"):
      return mediaPath;
    default:
      return `${process.env.NEXT_PUBLIC_MEDIA_URL}${mediaPath}`;
  }
};

// Function to remove duplicates
const removeDuplicates = (array, key) => {
  const seen = new Set();
  return array.filter((item) => {
    const keyValue = item[key];
    if (seen.has(keyValue)) {
      return false;
    } else {
      seen.add(keyValue);
      return true;
    }
  });
};

function formatDuration(duration) {
  // Remove the "s" suffix and convert to a number
  const totalSeconds = parseInt(duration.replace("s", ""), 10);

  // Ensure the duration is a valid number
  if (isNaN(totalSeconds) || totalSeconds < 0) {
    throw new Error("Invalid duration format");
  }

  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  let formattedDuration = "";

  if (hours > 0) {
    formattedDuration += `${hours}h `;
  }

  if (minutes > 0 || hours > 0) {
    // show minutes if there are hours even if minutes are zero
    formattedDuration += `${minutes}m `;
  }

  formattedDuration += `${seconds}s`;

  return formattedDuration.trim();
}

export { getMediaAbsolutePath, removeDuplicates, formatDuration };
