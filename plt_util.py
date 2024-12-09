import matplotlib.pyplot as plt
import seaborn as sns

def create_plots(audio, time, frequency, activation, confidence):
    # Set Seaborn theme for academic style
    sns.set_theme(style="whitegrid", palette="muted")
    colors = sns.color_palette("deep")

    # Calculate the average activation
    average_activation = activation.mean(axis=1)

    # Plotting all the graphs together in a grid
    fig, axs = plt.subplots(2, 2, figsize=(20, 16))

    # Plot Core Frequency
    axs[0, 0].plot(time, frequency, color=colors[0], linewidth=3)
    axs[0, 0].set_xlabel('Time (s)', fontsize=14)
    axs[0, 0].set_ylabel('Frequency (Hz)', fontsize=14)
    axs[0, 0].set_title('Core Frequency Over Time', fontsize=16)
    axs[0, 0].grid(visible=True, linestyle="--", alpha=0.6)

    # Plot Max Amplitude
    axs[0, 1].plot(audio, color=colors[1], linewidth=3)
    axs[0, 1].set_xlabel('Sample Rate Index (length)', fontsize=14)
    axs[0, 1].set_ylabel('Amplitude', fontsize=14)
    axs[0, 1].set_title('Amplitude Over Time', fontsize=16)
    axs[0, 1].grid(visible=True, linestyle="--", alpha=0.6)

    # Plot Average Activation
    axs[1, 0].plot(time, average_activation, color=colors[2], linewidth=3)
    axs[1, 0].set_xlabel('Time (s)', fontsize=14)
    axs[1, 0].set_ylabel('Average Activation', fontsize=14)
    axs[1, 0].set_title('Average Activation Over Time', fontsize=16)
    axs[1, 0].grid(visible=True, linestyle="--", alpha=0.6)

    # Plot Confidence
    axs[1, 1].plot(time, confidence, color=colors[3], linewidth=3)
    axs[1, 1].set_xlabel('Time (s)', fontsize=14)
    axs[1, 1].set_ylabel('Confidence', fontsize=14)
    axs[1, 1].set_title('Confidence Over Time', fontsize=16)
    axs[1, 1].grid(visible=True, linestyle="--", alpha=0.6)

    # Improve layout
    plt.tight_layout()
    plt.savefig('plots/transparent/all_plots_grid.png', transparent=True)
    plt.show()


def violin_plot(data):
    _, axes = plt.subplots(2, 2, figsize=(12, 10))

    for ax, column in zip(axes.flat, data.columns[:-1]):  # Exclude 'label'
        sns.violinplot(data=data, x='label', y=column, ax=ax, palette='Set2', hue='label', legend=False)
        ax.set_title(f'Distribution Of {column.replace("_", " ").title()} By Label', fontsize=12)
        ax.set_xlabel('Label', fontsize=10)
        ax.set_ylabel(column.replace("_", " ").title(), fontsize=10)

    plt.tight_layout()
    plt.show()

def correlation_matrix(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.drop('label', axis=1).corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix', fontsize=16)
    plt.show()
