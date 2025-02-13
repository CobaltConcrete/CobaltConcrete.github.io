async function insertUserWithFetch() {
  const response = await fetch('https://your-supabase-url.supabase.co/rest/v1/rpc/insert_user', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'apikey': 'your-supabase-key',
      'Authorization': `Bearer your-supabase-key`,
    },
    body: JSON.stringify({
      name: 'Alice',
      age: 25,
      genderid: 1,
      description: 'Developer',
      picture: 'picture_url',
      credits: 100,
    }),
  });

  const data = await response.json();
  if (!response.ok) {
    console.error('Error inserting user:', data);
  } else {
    console.log('User inserted successfully:', data);
  }
}

insertUserWithFetch();
