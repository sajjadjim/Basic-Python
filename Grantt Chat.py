import pandas as pd   
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define the data
data = {
    "Task": [
        "Planning and Requirements",
        "Design",
        "Development",
        "Testing",
        "Deployment and Rollout",
        "Maintenance and Support"
    ],
    "Start Time": [
        "2024-06-01",
        "2024-06-20",
        "2024-07-13",
        "2024-09-13",
        "2024-10-13",
        "2024-11-02"
    ],
    "End Time": [
        "2024-06-18",
        "2024-07-13",
        "2024-09-09",
        "2024-10-13",
        "2024-11-04",
        "2024-12-12"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert Start Time and End Time to datetime
df["Start Time"] = pd.to_datetime(df["Start Time"])
df["End Time"] = pd.to_datetime(df["End Time"])

# Calculate the duration in days
df["Duration"] = (df["End Time"] - df["Start Time"]).dt.days

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create a color list for tasks
colors = plt.cm.Paired(range(len(df)))

# Add the tasks to the Gantt chart
for i, task in enumerate(df.itertuples()):
    ax.barh(task.Task, task.Duration, left=task._2, color=colors[i])
    ax.text(task._2 + pd.Timedelta(days=task.Duration / 2), i, f"{task.Duration} days", 
            va='center', ha='center', color='white', fontweight='bold')

# Format the x-axis
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Task')
ax.set_title('Project Schedule Gantt Chart')

plt.tight_layout()
plt.show()
