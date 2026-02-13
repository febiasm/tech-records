import { useEffect, useState } from "react";

type Profile = {
  name: string;
  health: string;
  version: number;
};

function Homepg() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  fetch("http://localhost:8000/profile")
    .then((res) => {
      console.log("STATUS:", res.status);
      return res.json();
    })
    .then((data) => {
      console.log("DATA:", data);
      setProfile(data);
      setLoading(false);
    })
    .catch((err) => {
      console.error("FETCH ERROR:", err);
      setLoading(false);
    });
}, []);

  if (loading) return <p>Loading...</p>;
  if (!profile) return <p>No data</p>;

  return (
    <div>
      <h1>Backend Data</h1>
      <p>
         {profile.name}
      </p>
      <p>Status: {profile.health}</p>
      <p>version: {profile.version}</p>
    </div>
  );
}

export default Homepg;
