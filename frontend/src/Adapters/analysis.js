import axios from "axios";

export async function getTweetData(hashtag) {
  try {
    const data = await axios.get(`http://localhost:8000/tweet/${hashtag}`);
    return data.data;
  } catch (error) {
    console.log(error);
  }
}

export async function getRedditData(post_id) {
  try {
    const data = await axios.get(
      `http://localhost:8000/reddit/post/${post_id}`
    );
    return data.data;
  } catch (error) {
    console.log(error);
  }
}
